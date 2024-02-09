## Authors

 - Dusan Djordjevic SV1/2021
 - Stefan Pejinovic SV13/2021
 - Nikola Maric SV69/2021
 - Petar Simeunovic SV76/2021

## Plugins

 - Block visualizer
 - Simple visualizer
 - Data source github
 - Data source tiktok

## Venv(virtual envoirment)
    - It is recommended to use a virtual environment
    - To make venv use this command:
        ```console
        root@username:~$/SOK py -m venv .env
        ```
    - After this you should activate env in your terminal with this command:
        ```console
        root@username:~$/SOK ./.env/Scripts/activate
        (.env)root@username:~$ 
        ```

## How to install pip dependencies?
    - Use requirements.txt for that purpose after 
        ```console
        (.env)root@username:~$/SOK pip install -r requirements.txt
        ```
## How to install plugins?
    - Each plugin is started by placing it in the root folder of the plugin containing pyproject.toml and running the command
         ```console
        (.env)root@username:~$/SOK/data_source_github pip install -e .
        ```
## How to start Django app?
    ```console
        root@username:~$/SOK/graph_explorer py manage.py runserver
    ```