import React from 'react';

const Login = () => {
    return (
        <div className="container mt-5 align-content-center">

            <div className="row justify-content-center">
                <div className="col-md-7 col-lg-5">
                    <div className="login-wrap p-4 p-md-5">
                        <div className="icon d-flex align-items-center justify-content-center">
                            <span className="fa fa-user-o"></span>
                        </div>
                        <h3 className="text-center mb-4">Iniciar sesión</h3>
                        <form action="#" className="login-form">
                            <div className="form-group">
                                <input type="text" className="form-control rounded-left" placeholder="Usuario" required="True"></input>
                            </div>
                            <div className="form-group d-flex">
                                <input type="password" className="form-control rounded-left" placeholder="Contraseña" required="True"></input>
                            </div>
                            <div className="form-group">
                                <button type="submit" className="form-control btn btn-primary rounded submit px-3">Aceptar</button>
                            </div>
                          {/*  <div className="form-group d-md-flex">

<div className="w-50 text-md-right">
<a href="#">Forgot Password</a>
    </div>
                            </div>*/}
                        </form>
                    </div>
                </div>
            </div>
        </div>
    );
}
export default Login;