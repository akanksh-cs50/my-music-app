# Backend (Python Flask, FFmpeg)

### Flask

Flask will be used to make an api with the routes /arists, /songs, /albums.
Each route will have 'q' as a parameter to query or return all items if no parameters are specificed.


### FFmpeg

FFmpeg's ffprobe tool will be used to extract the artist info from file tags as my MusicPD directory structure is like <Album>/<Song>

```bash
ffprobe -v quiet -print_format json -show_format -show_streams file.mp4 | jq -r '.format.tags.artist'
```

This command will help us get the artist's name
