import React from 'react';
import Buscador from './Buscador';

const Clientes = () => {
    return (
        <div>
            <h3>Clientes</h3><hr></hr>
            <Buscador />
            <br></br>
            <table className="table table-bordered border-dark">
                <thead>
                    <tr>
                        <th scope="col">Cliente</th>
                        <th scope="col">Domicilio</th>
                        <th scope="col">Telefono</th>
                        <th scope="col">Mail</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">Franco Morello</th>
                        <td>Boedo 1089, Bernal</td>
                        <td>0800-2222</td>
                        <td>franco@gmail.com</td>
                    </tr>
                </tbody>
            </table>
            <button className="btn btn-primary">Nuevo cliente</button>
            <button className="btn btn-primary">Modificar cliente</button>
            <button className="btn btn-primary">Eliminar cliente</button>
        </div>
    );
}
 
export default Clientes;