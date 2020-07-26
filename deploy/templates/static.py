{{ with secret "secrets/spaces/access" }}
AWS_ACCESS_KEY_ID = '{{ .Data.AWS_ACCESS_KEY_ID }}' 
AWS_SECRET_ACCESS_KEY = '{{ .Data.AWS_SECRET_ACCESS_KEY }}' 
{{ end }}