import React from 'react';
import Datepicker from "./Datepicker";

const Turnos = () => {
    return (
        <div>
            <h3>Turnos del dia:</h3>
            <Datepicker />
            <hr></hr>
            <table className="table table-bordered border-dark">
                <thead>
                    <tr>
                        <th scope="col">Cliente</th>
                        <th scope="col">Nombre del animal</th>
                        <th scope="col">Raza</th>
                        <th scope="col">Peso</th>
                        <th scope="col">Hora</th>
                        <th scope="col">Peluquero</th>
                        <th scope="col">Monto</th>
                        <th scope="col">Abonado</th>
                        <th scope="col">Observaciones</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">Mark</th>
                        <td>Tino</td>
                        <td>Calle</td>
                        <td>10kg</td>
                        <td>17:45</td>
                        <td>Horacio</td>
                        <td>Monto</td>
                        <td><input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input></td>
                        <td>Problema de piel</td>
                    </tr>
                </tbody>
            </table>
            <button className="btn btn-primary">Nuevo turno</button>
            <button className="btn btn-primary">Modificar turno</button>
            <button className="btn btn-primary">Eliminar turno</button>
        </div>
        );
}
 
export default Turnos;