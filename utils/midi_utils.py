# midi_utils.py

from mido import MidiFile, MidiTrack, Message
import os


def generate_midi(star_data, constellation):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    for star in star_data:
        pitch = star['pitch']
        duration = star['duration']
        track.append(Message('note_on', note=pitch, velocity=64, time=0))
        track.append(Message('note_off', note=pitch, velocity=64, time=duration))

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{constellation}_music.mid")
    midi.save(file_path)
    return file_path