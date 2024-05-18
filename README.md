# Python Database Application

This repository contains a Python web application that connects to a MySQL database. It's designed to demonstrate a simple CRUD (Create, Read, Update, Delete) application using Flask and MySQL.

## Prerequisites

Before running this application, ensure you have the following installed:

- Docker
- Docker Compose

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone git@github.com:asirabdelhady/python-db-app.git
   ```

2. Navigate into the cloned repository directory:

   ```bash
   cd python-db-app
   ```

3. Modify the `app.py` file:

   - Open the `app.py` file in a text editor.
   - Locate the `db_config` dictionary and update it with your MySQL database configuration. Change the `host`, `user`, `password`, and `database` fields according to your MySQL setup.

4. Run the application using Docker Compose:

   ```bash
   docker-compose up --build
   ```

5. Access the application:

   Once the Docker containers are up and running, you can access the application at [http://localhost:5000](http://localhost:5000) in your web browser.

## Troubleshooting

### Database Connection Issues

If you encounter errors related to database connection, such as "Can't connect to MySQL server" or similar, it may be due to MySQL server configuration.

1. **Check MySQL Server Binding**: By default, MySQL may be bound to `localhost` or `127.0.0.1`, which restricts connections from outside the local machine. To allow connections from other hosts, you may need to comment out or modify the `bind-address` configuration in your MySQL server configuration file (`my.cnf` or `mysqld.cnf`). You can find this file typically in `/etc/mysql` or `/etc/mysql/mysql.conf.d` directory.

2. **Restart MySQL Server**: After making changes to the MySQL server configuration, restart the MySQL server to apply the changes.

### Still Having Issues?

If you're still experiencing issues after following these steps, feel free to [open an issue](https://github.com/asirabdelhady/python-db-app/issues) on GitHub, and we'll be happy to assist you further.
