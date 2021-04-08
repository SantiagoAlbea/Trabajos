import React, { useState } from "react";
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";
import { Container, Row, Col } from "react-bootstrap";

const Datepicker = () => {
  const [startDate, setStartDate] = useState(new Date());
  return (
    <div className="DatePicker">
      <Container fluid>
        <Row>
          <Col>
            <DatePicker
              selected={startDate}
              onChange={date => setStartDate(date)}
            />
            {/*<p>{startDate.toString()}</p>*/}
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Datepicker;