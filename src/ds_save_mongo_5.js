use myDB
show dbs
show tables
db.myCol.insert({"Persons":[{"id":"20151113","이름":"서창희"},{"id":"201511079","이름":"강은다"}]})
db.myCol.find({"Persons.이름":"서창희"})