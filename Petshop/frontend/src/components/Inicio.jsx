import React from 'react';

const Inicio = () => {
    return (
        <div className="container-fluid">
            <div className="row justify-content-between mt-5">
                <div className="col-4 border border-primary">
                    <iframe src="https://calendar.google.com/calendar/embed?height=600&amp;wkst=1&amp;bgcolor=%23ffffff&amp;ctz=America%2FArgentina%2FBuenos_Aires&amp;src=NGowbDlhYXJrcW91MmwwMjhncDdwZ2sxdDhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;src=ZXMuYXIjaG9saWRheUBncm91cC52LmNhbGVuZGFyLmdvb2dsZS5jb20&amp;color=%23EF6C00&amp;color=%230B8043&amp;title=Hakuna%20Matata&amp;showPrint=0&amp;showCalendars=0&amp;showTz=0" styleName="border:solid 1px #777" width="100%" height="400" frameborder="0" scrolling="no"></iframe>
                </div>
                <div className="col-4 border border-primary">
                    <ul>
                        <li>Stock bajo de dog chow</li>
                    </ul>
                </div>
                <div className="col-2 border border-primary text-center">
                    <h4>Comentarios</h4>
                </div>
            </div>
            
        </div>
    );
}
 
export default Inicio;