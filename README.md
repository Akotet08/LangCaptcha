# LangCaptcha

## How to run the backend and DB server

1. Spin up a Postgres database and the backend in containers. From the project root directory, run:

    ```shell
    cd backend && docker compose up  # use the --build flag if this is your first time spinning up the project
    ```

2. Make sure that the containers are running using

    ```shell
    docker ps
    ```

    If this is the first time you set up the environment, save the authentication data into the database by running

    ```shell
    cd ../utils
    python preprocess_first_text.py
    ```

    This will create the data table `first` in the database and populate it with English-Korean parallel corpus data. The table will look like

    | id | en      | ko      |
    |----|---------|---------|
    | 1  | text in | text in |
    | 2  | english | korean  |

    To set up the second part of the verification, run

    ```shell
    cd utils
    python setup_second.py
    ```

    This will create the prompt pool data `prompt` and populate it with three sample prompts.

     id |                                        text
    ----|------------------------------------------------------------------------------------
      1 | I cannot find my umbrella.
      2 | Where is the organizer of this event
      3 | There should be a policy that limits the number of visitors in the school per day.

    It will also create a table to store the translations submitted in the second part, `second`.

    | id | prompt_id      | translation      |
    |----|----------------|------------------|

    In order to check if the tables are created, you can enter the container using the command

    ```shell
    docker exec -it <postgres-container-id> psql -U postgres -d bytes
    ```
