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
import Login from "./components/Login";


function App() {
  return (
    <Router>
{/*       <Login /> */}
      <div className="container-fluid">
        <div className="row mt-5 justify-content-between">
          <div className="btn-group col-7">
            <NavLink to="/" className="btn btn-primary" activeClassName="active">Inicio</NavLink>
            <NavLink to="/ventas" className="btn btn-primary" activeClassName="active">Ventas</NavLink>
            <NavLink to="/turnos" className="btn btn-primary" activeClassName="active">Turnos</NavLink>
            <NavLink to="/stock" className="btn btn-primary" activeClassName="active">Stock</NavLink>
            <NavLink to="/clientes" className="btn btn-primary" activeClassName="active">Clientes</NavLink>
            <NavLink to="/proveedores" className="btn btn-primary" activeClassName="active">Proveedores</NavLink>
          </div>
          <div className="col-1">
            <div class="btn-group">
              <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                Pelado
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Editar Perfil</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
                <li><hr class="dropdown-divider"></hr></li>
                <li><a class="dropdown-item" href="#">Cerrar Sesión</a></li>
              </ul>
            </div>
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
