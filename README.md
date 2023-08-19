# LangCaptcha

## How to run the DB server

1. Spin up a Postgres database in a container. In the root directory, run

    ```shell
    docker compose up
    ```

2. `Save the authentication data into the database by running

    ```shell
    cd utils
    python preprocess_first_text.py
    ```

    The data table `first` will look like

    | id | en      | ko      |
    |----|---------|---------|
    | 1  | text in | text in |
    | 2  | english | korean  |
