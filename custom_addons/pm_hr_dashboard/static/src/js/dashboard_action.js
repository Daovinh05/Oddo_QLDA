/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, xml } from "@odoo/owl";

export class PmHrDashboardIframe extends Component {
    static template = xml`
        <div class="o_action" style="width: 100%; height: 100%; overflow: hidden; background: #f8fafc;">
            <iframe src="/pm_hr/dashboard_view" style="width: 100%; height: calc(100vh - 50px); border: none;"></iframe>
        </div>
    `;
}

registry.category("actions").add("pm_hr_dashboard_client_action", PmHrDashboardIframe);
