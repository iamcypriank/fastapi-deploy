# Deployment Guide


# elastic beanstalk doesnt support prproject.toml
 - use  [ uv export --format requirements-txt --no-hashes -o requirements.txt ]
 - to generate  requirements.txt
 - and use this command to generate pdf 
 zip -r app.zip . \
-x ".git/*" \
-x ".venv/*" \
-x "__pycache__/*"