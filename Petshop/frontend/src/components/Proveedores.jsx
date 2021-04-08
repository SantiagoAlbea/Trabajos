import React from 'react';
import Buscador from './Buscador';

const Proveedores = () => {
    return (
        <div>
            <h3>Proveedores</h3><hr></hr>
            <Buscador />
            <br></br>
            <table className="table table-bordered border-dark">
                <thead>
                    <tr>
                        <th scope="col">Proveedor</th>
                        <th scope="col">Domicilio</th>
                        <th scope="col">Telefono</th>
                        <th scope="col">Telefono alternativo</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">DogChow</th>
                        <td>Boedo 1089, Bernal</td>
                        <td>0800-dogchow</td>
                        <td>0800-123123</td>
                    </tr>
                </tbody>
            </table>
            <button className="btn btn-primary">Nuevo Proveedor</button>
            <button className="btn btn-primary">Modificar Proveedor</button>
            <button className="btn btn-primary">Eliminar Proveedor</button>
        </div>
    );
}
 
export default Proveedores;