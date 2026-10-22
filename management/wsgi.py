import utils.net
import utils.clients
import utils.http_session
import utils.transport
import utils.session
from daemon import app
import utils

app.logger.addHandler(utils.create_syslog_handler())

if __name__ == "__main__":
    app.run(port=10222)
