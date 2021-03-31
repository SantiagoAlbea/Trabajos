import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  NavLink
} from "react-router-dom";
import Stock from "./components/Stock";
import Inicio from "./components/Inicio";
import Clientes from "./components/Clientes";
import Proveedores from "./components/Proveedores";
import Turnos from "./components/Turnos";
import Ventas from "./components/Ventas";

function App() {
  return (
    <Router>
      <div className="container-fluid mt-5">
        <div className="row">
          <div className="btn-group col-4">
            <NavLink to="/" className="btn btn-primary" activeClassName="active">Inicio</NavLink>
            <NavLink to="/ventas" className="btn btn-primary" activeClassName="active">Ventas</NavLink>
            <NavLink to="/turnos" className="btn btn-primary" activeClassName="active">Turnos</NavLink>
            <NavLink to="/stock" className="btn btn-primary" activeClassName="active">Stock</NavLink>
            <NavLink to="/clientes" className="btn btn-primary" activeClassName="active">Clientes</NavLink>
            <NavLink to="/proveedores" className="btn btn-primary" activeClassName="active">Proveedores</NavLink>
          </div>
          <div className="col-2 justify-content-between align-items-center">
            <button className="btn btn-primary ml-auto">Boton</button>
          </div>
        </div>
        <hr />
        <Switch>
          <Route path="/stock">
            <Stock />
          </Route>
          <Route path="/ventas">
            <Ventas />
          </Route>
          <Route path="/turnos">
            <Turnos />
          </Route>
          <Route path="/clientes">
            <Clientes />
          </Route>
          <Route path="/proveedores">
            <Proveedores />
          </Route>
          <Route path="/" exact>
            <Inicio />
          </Route>
        </Switch> 
      </div>
    </Router>
  );
}

export default App;
