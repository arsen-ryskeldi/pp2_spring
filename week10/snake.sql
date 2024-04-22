CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE
);

CREATE TABLE user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user(id),
    level INTEGER,
    score INTEGER,
    paused BOOLEAN
);
