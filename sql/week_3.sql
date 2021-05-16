create table books_with_prices
(
    id    int auto_increment primary key,
    title varchar(10),
    price decimal(15, 2)
);

create table buyer
(
    id     int auto_increment primary key,
    `name` varchar(15)
);

create table book_bought
(
    book_id  int,
    buyer_id int,

    foreign key (book_id) references books_with_prices (id) on update cascade on delete cascade,
    foreign key (buyer_id) references buyer (id) on update cascade on delete cascade
);

insert into books_with_prices(title, price) values
('wretth', 12.9),
('ytj', 6456.75),
('geerge', 6456.75),
('yegtryhtj', 6456.75),
('jtytyngh', 32.9),
('hnhgn', 15.9),
('uuggh', 24.9),
('gnhntj', 1.9),
('gnhntj', 1.9),
('wefgerg', 1.9),
('gnergrthh', 1.9),
('urtujn', 756.9);

insert into buyer (name) values 
('ewfgergr'),
('ewfgrer'),
('ewfgeyj'),
('ewfgu76'),
('ewfgrjy'),
('ewfhrthg'),
('ewrgtgfg'),
('grt');

insert into book_bought (book_id, buyer_id)
values (1, 1),
 (1, 2),
 (1, 3),
 (1, 4),
 (2, 4),
 (5, 4),
 (3, 2);

insert into book_bought (book_id, buyer_id)
values (3, 5);

-- ile książek w ogóle
select count(id) from books_with_prices;

-- ile kupionych książek w ogóle
select count(id) from books_with_prices
inner join book_bought bb on books_with_prices.id = bb.book_id;

-- ile kupionych egzemplarzy danej książki
select count(id) as book_copy, title from books_with_prices
inner join book_bought bb on books_with_prices.id = bb.book_id
group by id;


select title, price, count(id) as sold, sum(price) as income from books_with_prices
inner join book_bought bb on books_with_prices.id = bb.book_id
group by id;

-- wybierz książkę o najniższej cenie
select title, price
from books_with_prices
group BY title, price
order by price limit 1;

select min(price)
from books_with_prices;

-- najdroższa książka
select title, price
from books_with_prices
group BY title, price
order by price desc limit 1;

select max(price) from books_with_prices;

select count(id), min(price) from books_with_prices
group by price;

select count(id) from books_with_prices
where price = (select min(price) from books_with_prices);

select id, title from books_with_prices
where price = (select min(price) from books_with_prices);

select count(id) as book_copy, title, price from books_with_prices
inner join book_bought bb on books_with_prices.id = bb.book_id
where price = (select min(price) from books_with_prices)
group by id;