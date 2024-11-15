"""
create table STOCK(
    Pno int primary key,
    Pname varchar(50),
    Dcode int,
    Qty int,
    UnitPrice int,
    StockDate date
);

create table DEALERS(
    Dcode int,
    Dname varchar(60)
);

insert into STOCK values(
    5005,
    'Ball point pen',
    102,
    100,
    10,
    '2021-03-31'
);

insert into STOCK values(
    5003,
    'Gell pen premium',
    102,
    150,
    15,
    '2021-01-01'
);

insert into STOCK values(
    5002,
    'Pencil',
    101,
    125,
    14,
    '2021-02-18'
);

insert into STOCK values(
    5006,
    'Scale',
    101,
    200,
    6,
    '2020-01-01'
);

insert into STOCK values(
    5001,
    'Eraser',
    102,
    210,
    3,
    '2020-03-19'
);

insert into STOCK values(
    5004,
    'Sharpener',
    102,
    60,
    5,
    '2020-12-09'
);

insert into STOCK values(
    5009,
    'Gel pen classic',
    103,
    160,
    8,
    '2022-01-19'
);

insert into DEALERS values(101,'Sakthi Stationeries');

insert into DEALERS values(103,'Classic Stationeries');

insert into DEALERS values(102,'Indian Book House');
"""