CREATE TABLE projects
(
    project_id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    project_name TEXT,
    summary TEXT,
    details TEXT,
    tags TEXT[],
    start_date date,
    end_date date
);