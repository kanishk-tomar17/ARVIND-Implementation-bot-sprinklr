# Voice Recordings — Stereo Channel (Agent/Customer) Swap

**Source:** Field work on Qatar Rail call-recording import, 2026-08-16. Confirmed by the consultant from a prior import that Sprinklr's channel convention is the **opposite** of the source recorder's output.

## The problem
Telephony call recordings are usually **2-channel (stereo)**: one channel carries the agent, the other the customer. Sprinklr uses that separation for **diarized transcription** — labelling who said what.

If the source recorder's channel order is the reverse of what Sprinklr expects, every imported call comes out with **agent and customer speech attributed to the wrong speaker**. Nothing errors; the import "succeeds". It quietly corrupts transcripts, sentiment, and any QA scoring built on top.

## There is no Sprinklr-side setting for this
Checked and confirmed absent:
- Data Connector → **Entity Specific Settings for Voice Cases** (only Account Type, Account, Default Language, Disable Transcription)
- Data Connector → **Source Specific Settings** (only file format, metadata type, recording type, encryption)
- No match for `diariz*` / `speaker` / `channel map` anywhere in `sprinklr-map.json`

**So the fix belongs on the file side, before zipping.**

## How to verify before bulk-importing
Import 1–2 calls unswapped, open the resulting case, and check the transcript/audio player to see which channel Sprinklr labels agent vs customer. Only swap the rest if it's genuinely reversed. (Skip this only when the same client/recorder combination has already been proven reversed.)

## How to swap (no ffmpeg needed for PCM WAV)
Standard telephony WAVs are 8 kHz, 16-bit, 2-channel PCM — Python's stdlib `wave` handles them, so no ffmpeg dependency:

```python
import wave
with wave.open(src, 'rb') as wf:
    params, frames = wf.getparams(), wf.readframes(wf.getnframes())
ba = bytearray(frames)
for i in range(len(ba) // 4):          # 4 bytes/frame = 2ch x 16-bit
    off = i * 4
    ba[off:off+2], ba[off+2:off+4] = ba[off+2:off+4], ba[off:off+2]
with wave.open(dst, 'wb') as out:
    out.setparams(params); out.writeframes(bytes(ba))
```

Write to a **new folder**, never overwrite the originals — the swap must stay reversible.

## Verifying the swap actually worked
Do **not** just check that the files differ. Silence is identical on both channels, so a naive byte-compare or a check on the opening frames can pass on a file that was never swapped. Find frames where **L != R** in the original and assert `swapped.L == original.R` and `swapped.R == original.L`:

```python
lo, ro = struct.unpack('<hh', orig[off:off+4])
ls, rs = struct.unpack('<hh', swap[off:off+4])
if lo != ro:                      # only meaningful on non-silent frames
    assert ls == ro and rs == lo
```

## Notes / gaps
- Sample rate/width assumptions: the loop above is specific to **16-bit stereo**. Guard on `getsampwidth() == 2` and `getnchannels() == 2` and fail loudly otherwise.
- Feeds [[unified-data-connector-voice-import]].
