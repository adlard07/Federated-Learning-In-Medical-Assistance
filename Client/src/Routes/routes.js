import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom"

import Login from "../Pages/Login";
import Dashboard from "../Pages/Dashboard";
import Register from "../Pages/Register";
import AdminPage from "../Pages/AdminPage";
import "../Styles/routes.css"

const logado = localStorage.getItem('@user');

const Rotas = () => {
    return (
        <BrowserRouter>
            <Routes>
                {logado && <Route path="/" element={<Dashboard />} />}
                {logado && <Route path="/admin" element={<AdminPage />} />}
                {!logado && <Route path="/login" element={<Login logado={logado} />} />}
                {!logado && <Route path="/register" element={<Register logado={logado} />} />}
            </Routes>
        </BrowserRouter>
    );
};

export default Rotas;