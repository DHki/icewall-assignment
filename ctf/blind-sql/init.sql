CREATE TABLE users(
    id char(32) primary key,
    passwd char(64)
);

INSERT INTO users (id, passwd) VALUES ('admin', '**FLAG**');
INSERT INTO users (id, passwd) VALUES ('guest', 'guest');