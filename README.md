# Data Warehouse ETL process with Apache Airflow

---

With this project I will extract, transform and load Data into a Data Warehouse database created using Docker and Postgres.
Pipelines and Data Warehousing process of a Data Engineer's life, lovely.

---

This project is made as a activity of the Data Engineering course, Design and Implementation of Data Warehouses, by Data Science Academy.

---

Softwares used to this:

- postgres docker image on dockerhub: `https://hub.docker.com/_/postgres` or with command `docker pull postgres`;
- Anaconda python: `https://www.anaconda.com`;
- pgAdmin: `https://www.pgadmin.org`;
- Apache Airflow (with Docker): `https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html`

---

With postgres image I create the databse through Docker using the command:
`docker run --name dsalabdw -p 5433:5432 -e POSTGRES_USER=vinicius_arantes -e POSTGRES_PASSWORD=vini170500 -e POSTGRES_DB=dwdb -d postgres`

After created, I create the pgAdmins server, a new database called `dwdb` and a new schema called `dsalabdw`

---

For Airflow I use the docker version following the documentation avaliable on `https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html`, the .yaml file required is in this repo.

---

To connect both the containers of Airflow and postgres I use the command:
`docker network disconnect bridge (container_name_postgres)`
`docker network connect {container_name_airflow} {container_name_postgres}`
Also, will be much easier to first up the airflow containers and then create the postgres on the same network using `--network`.

---

This is a super simple example to pratice the DAG creation and Airflow use cases in Real world. Is a simple SQL execution, but can be optimizated to almost any ETL process that uses SQL.
