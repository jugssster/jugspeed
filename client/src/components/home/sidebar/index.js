import React from "react";
import SidebarItem from "./SidebarItem";
import "./style.css";
const Sidebar = () => {
  return (
    <div className="sidebar">
      <SidebarItem title="Featured" icon="fab fa-500px" count="90" />
      <SidebarItem title="advertising" icon="fas fa-address-book" count="20" />
      <SidebarItem title="analytics" icon="fab fa-alipay" count="34" />
      <SidebarItem title="attribution" icon="fas fa-archive" count="15" />
      <SidebarItem title="live chat" icon="fas fa-address-book" count="66" />
      <SidebarItem title="mobile" icon="fab fa-500px" count="57" />
    </div>
  );
};
export default Sidebar;