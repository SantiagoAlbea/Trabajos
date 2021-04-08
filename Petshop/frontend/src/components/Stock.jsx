import React from 'react';
import Buscador from './Buscador';

const Stock = () => {
    return (
        <div>
            <h3>Stock</h3><hr></hr>
            <Buscador />
            <br></br>
            <table className="table table-bordered border-dark">
                <thead>
                    <tr>
                        <th scope="col">Descripcion</th>
                        <th scope="col">Stock</th>
                        <th scope="col">Proveedor</th>
                        <th scope="col">Precio</th>
                        <th scope="col">Precio por bulto</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">Dog Chow Adultos</th>
                        <td>4</td>
                        <td>
                            <a>DogChow</a>
                        </td>
                        <td>$1000</td>
                        <td>$1000</td>
                    </tr>
                </tbody>
            </table>
            <button className="btn btn-primary">Nuevo producto</button>
            <button className="btn btn-primary">Modificar producto</button>
            <button className="btn btn-primary">Eliminar producto</button>
        </div>
    );
}
 
export default Stock;