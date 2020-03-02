import React, { Component } from 'react';
import { Grid, List, ListItem, Link } from '@material-ui/core';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="root-container">
        <Grid container className="header-container" justify="center" alignItems="center">
          <p>INST ®</p>
        </Grid>
        <Grid container className="body-container" justify="center">
          <List>
            <ListItem className="list-item">
              <p>Olexandr Hnennyi</p>
            </ListItem>
            <ListItem className="list-item">
              <p>Vladoos Bobrovskyi</p>
            </ListItem>
            <ListItem className="list-item">
              <p>Maxim Potapov</p>
            </ListItem>
          </List>
        </Grid>
        <Grid container className="footer-container" justify="center">
          <p>Reserved in Lviv - 2020</p>
        </Grid>
      </div>
    );
  }
}

export default App;
