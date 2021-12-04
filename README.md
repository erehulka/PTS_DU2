## Running the app

To install requirements, run

    pip3 install -r requirements.txt
    mkdir log

Then to setup database, run

    make create_whole_db

Now, your database is configured, and you can run all tests simply with `make`, which runs `make test`

Info: To also run database tests, you have to uncomment the method in test/testDB.py. Then run following three commands:

    make recreate_whole_db
    make
    make recreate_whole_db

### Make commands
There are some more make commands, which you can use when using the app.
|  Command | Action |
|--|--|
| `make recreate_whole_db`| Deletes whole database with all data and recreates it from scratch |
| `make create_db_delete_old` | Deletes and recreates only database schema, you can then choose which dataset you want to load into database |
|`make create_dataset_basic`| Loads Basic dataset into database (one line, six stops) |

## Config

To print database outputs set `Debug` to `True` in config.ini file.