import React from 'react';

const Ventas = () => {
    return (
        <div>
            <h3>Ventas</h3><hr></hr>
            <button className="btn btn-primary">Nueva venta</button>
            <h5>Ventas de hoy</h5>
            <table className="table table-bordered border-dark">
                <thead>
                    <tr>
                        <th scope="col">Cliente</th>
                        <th scope="col">Monto total</th>
                        <th scope="col">Usuario</th>
                        <th scope="col">Vendedor</th>
                        <th scope="col">Hora</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">Mark</th>
                        <td>$1500</td>
                        <td>Pelado</td>
                        <td>Pelado</td>
                        <td>20:45</td>
                    </tr>
                    <tr>
                        <th scope="row">Total del dia:</th>
                        <td colSpan="4">$1500</td>
                    </tr>
                </tbody>
            </table>
            <button className="btn btn-primary">Modificar venta</button>
            <button className="btn btn-primary">Eliminar venta</button>
        </div>
    );
}
 
export default Ventas;