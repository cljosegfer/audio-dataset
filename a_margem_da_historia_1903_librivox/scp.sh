for f in *; do whisper $f  --device cuda  --language Portuguese --model large ; done
