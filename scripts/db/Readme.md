# Database backups / imports

## Create dump

execute `create-dump.py` and provide the following arguments

- `--container, -c` => The name or id of the docker pg container
- `--user, -u` => The name of the Postgres user (as specified in `.env`)
- `--database, --d` => The name of the database (as specified in `.env`)
  Example:

```
python create-dump.py --c my_pg_container --u batman --d gotham_database;
```

The script will log in to the postgres container and execute the `pg_dump` command in order to generate an sql dump file. The dump file will be stored in the `dumps` directory.

## Importing a dump

execute `import-dump.py` and provide the following arguments

- `--container, -c` => The name or id of the docker pg container
- `--user, -u` => The name of the Postgres user (as specified in `.env`)
- `--database, --d` => The name of the database (as specified in `.env`)
- `--file, --f` => The path to the sql dump file you want to import
  Example:

```
python import-dump.py --c my_pg_container --u batman --d gotham_database --f ./../../dumps/my_dump.sql;
```

This command will log in to the postgres container and execute the `pg_restore` command in order to import the specified dump file.
