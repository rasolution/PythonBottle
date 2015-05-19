<!DOCTYPE html>
<html>
<head lang="es">
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="http://localhost/Bottle/CSS/bootstrap.css"/>
    <script src="http://localhost/Bottle/JS/jquery-2.1.4.js"></script>
    <script src="http://localhost/Bottle/JS/index.js"></script>
    <title></title>
</head>
<body">
    <h1>Products</h1>
    <a href="/products/create"><button>Crear</button></a>
    <br/>
    <table id="products" class="table">
        <tr>
            <td><strong>ID</strong></td>
            <td><strong>Name</strong></td>
            <td><strong>Price</strong></td>
            <td><strong>Create</strong></td>
            <td><strong>Edit</strong></td>
        </tr>
    </table>

</body>
<script type="text/javascript">getProducts();</script>
</html>