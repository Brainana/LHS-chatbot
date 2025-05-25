echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > /app/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" >> /app/.streamlit/config.toml

sed -i "s/your-api-key-here/$OPENAI_API_KEY/" /app/.streamlit/secrets.toml
sed -i "s/your-claude-api-key-here/$CLAUDE_API_KEY/" /app/.streamlit/secrets.toml
sed -i "s/your-trubrics-email-here/$TRUBRICS_EMAIL/" /app/.streamlit/secrets.toml
sed -i "s/your-trubrics-pswd-here/$TRUBRICS_PASSWORD/" /app/.streamlit/secrets.toml

sed -i "s/chroma-ip-here/$CHROMA_IP/" /app/config_remotedb.json
sed -i "s/chroma-port-here/$CHROMA_PORT/" /app/config_remotedb.json
sed -i "s/doc-webserver-url-here/$DOC_WEBSERVER_URL/" /app/config_remotedb.json





