--TSQL NOTE:
--AUTHOR: EVAN


--1.Combine insert and select

INSERT INTO Person.ContactType
(
    Name,
    ModifiedDate
)
SELECT a.Name, a.ModifiedDate
FROM Person.AddressType a

--2. TOP

INSERT INTO Person.ContactType
(
    Name,
    ModifiedDate
)
SELECT TOP 3 a.AddressLine1, a.ModifiedDate
FROM Person.Address 

or

INSERT TOP(3) INTO Person.ContactType
(
    Name,
    ModifiedDate
)
SELECT a.AddressLine1, a.ModifiedDate
FROM Person.Address 

--3. UPDATE WITH JOIN

UPDATE Person.ContactType
SET Name = at.rowguid
FROM Person.ContactType ct
INNER JOIN Person.AddressType at
on ct.Name = at.Name

-- update with top
UPDATE TOP(2) Person.ContactType
SET 
    Name = ContactTypeID
WHERE ContactTypeID > 20

-- 4. DELETE

DELETE 
FROM Person.ContactType 
WHERE ContactTypeID > 20

--DELETE WITH TOP
DELETE TOP(2) 
FROM Person.ContactType 
WHERE ContactTypeID > 20

--DELETE WITH JOIN
DELETE FROM Person.ContactType 
FROM Person.ContactType ct
INNER JOIN Person.AddressType at 
on ct.Name = at.Name