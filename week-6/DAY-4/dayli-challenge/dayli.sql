create table items(
	item_id serial primary key,
	item_name varchar(200) not null,
	price int not null
);

create table users(
	user_id serial primary key,
	first_name varchar (100) not null
);

create table product_orders(
	order_id int not null,
	order_date date not null,
	item_id  serial primary key,
	user_id int not null,
	quantity int not null,
	constraint fk_user_id
	foreign key (user_id)
	references users(user_id)
	on delete cascade, 
	constraint fk_item_id
	foreign key (item_id)
	references items(item_id) 
	on delete cascade
);


