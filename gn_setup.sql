CREATE TABLE IF NOT EXISTS 
    employees (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(40) NOT NULL,
        last_name VARCHAR(40) NOT NULL,
        leader_id INTEGER,
        team_id INTEGER,
        title VARCHAR(10) NOT NULL,
        description VARCHAR(255) NOT NULL

        );

CREATE TABLE
    team (
    id INTEGER PRIMARY KEY,
    team_name VARCHAR(255),
    leader_id INTEGER,
    FOREIGN KEY(leader_id) REFERENCES employees(id)
    
    );