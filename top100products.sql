-- SQL Server T-SQL
SELECT TOP 100
    p.ProductID,
    p.Name,
    SUM(s.OrderQty) AS TotalSold
FROM Production.Product AS p
JOIN Sales.SalesOrderDetail AS s ON p.ProductID = s.ProductID
WHERE p.ModifiedDate > GETDATE() - 365
GROUP BY p.ProductID, p.Name
ORDER BY TotalSold DESC;