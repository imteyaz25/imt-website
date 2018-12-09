## imt-website


## Run gunicorn as below:
gunicorn --bind 0.0.0.0:8000 wsgi &

## Nginx settings:
<pre>
server {
    listen       80;

    server_name imteyaz.com;

    location / {

             proxy_pass         http://172.104.216.83:8000;
             proxy_redirect     off;
             proxy_set_header   Host $host;
             proxy_set_header   X-Real-IP $remote_addr;
             proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header   X-Forwarded-Host $server_name;

    }
}
</pre>
