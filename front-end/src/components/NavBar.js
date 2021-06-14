import React, { useState } from 'react'
import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink
  } from 'reactstrap';
function NavBar() {
    const [isOpen, setIsOpen] = useState(false);
    const toggle = () => setIsOpen(!isOpen);
    return (
        <Navbar className="p-3" color="light" light expand="md">
            <NavbarBrand >FixTix</NavbarBrand>
            <NavbarToggler onClick={toggle}/>
            <Collapse isOpen={isOpen} navbar>
                <Nav className="mr-auto" navbar>
                    <NavItem>
                        <NavLink >Dashboard</NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink>My Tickets</NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink>Login</NavLink>
                    </NavItem>
                </Nav>
            </Collapse>
      </Navbar>
    )
}

export default NavBar
