"use strict";

// Class definition
var KTDocsDatatableSubtable = function () {
    var table;
    var datatable;
    var template;

    // Private methods
    const initDatatable = () => {
        // Set date data order
        const tableRows = table.querySelectorAll('tbody tr');

        tableRows.forEach(row => {
            const dateRow = row.querySelectorAll('td');
            const realDate = moment(dateRow[1].innerHTML, "DD MMM YYYY, LT").format(); // select date from 2nd column in table

            // Skip template
            if (!row.closest('[data-kt-docs-datatable-subtable="subtable_template"]')) {
                dateRow[1].setAttribute('data-order', realDate);
                dateRow[1].innerText = moment(realDate).fromNow();
            }
        });

        // Get subtable template
        const subtable = document.querySelector('[data-kt-docs-datatable-subtable="subtable_template"]');
        template = subtable.cloneNode(true);
        template.classList.remove('d-none');

        // Remove subtable template
        subtable.parentNode.removeChild(subtable);

        // Init datatable --- more info on datatables: https://datatables.net/manual/
        datatable = $(table).DataTable({
            "info": false,
            'order': [],
            "lengthChange": false,
            'pageLength': 6,
            'ordering': false,
            'paging': false,
            'columnDefs': [
                { orderable: false, targets: 0 }, // Disable ordering on column 0 (checkbox)
                { orderable: false, targets: 6 }, // Disable ordering on column 6 (actions)
            ]
        });

        // Re-init functions on every table re-draw -- more info: https://datatables.net/reference/event/draw
        datatable.on('draw', function () {
            resetSubtable();
            handleActionButton();
        });
    }

    // Subtable data sample
    const data = [
        {
            image: '76',
            name: 'Go Pro 8',
            description: 'Latest  version of Go Pro.',
            cost: '500.00',
            qty: '1',
            total: '500.00',
            stock: '12'
        },
        {
            image: '60',
            name: 'Bose Earbuds',
            description: 'Top quality earbuds from Bose.',
            cost: '300.00',
            qty: '1',
            total: '300.00',
            stock: '8'
        },
        {
            image: '211',
            name: 'Dry-fit Sports T-shirt',
            description: 'Comfortable sportswear for everyday use.',
            cost: '89.00',
            qty: '1',
            total: '89.00',
            stock: '18'
        },
        {
            image: '21',
            name: 'Apple Airpod 3',
            description: 'Apple\'s latest and most advanced earbuds.',
            cost: '200.00',
            qty: '2',
            total: '400.00',
            stock: '32'
        },
        {
            image: '83',
            name: 'Nike Pumps',
            description: 'Apple\'s latest and most advanced headphones.',
            cost: '200.00',
            qty: '1',
            total: '200.00',
            stock: '8'
        }
    ];

    // Handle action button
    const handleActionButton = () => {
        const buttons = document.querySelectorAll('[data-kt-docs-datatable-subtable="expand_row"]');

        // Sample row items counter --- for demo purpose only, remove this variable in your project
        const rowItems = [ 1, 2];

        buttons.forEach((button, index) => {
            button.addEventListener('click', e => {
                e.stopImmediatePropagation();
                e.preventDefault();

                const row = button.closest('tr');
                const rowClasses = ['isOpen', 'border-bottom-0'];

                // Get total number of items to generate --- for demo purpose only, remove this code snippet in your project
                const demoData = [];
                for (var j = 0; j < rowItems[index]; j++) {
                    demoData.push(data[j]);
                }
                // End of generating demo data

                // Handle subtable expanded state
                if (row.classList.contains('isOpen')) {
                    // Remove all subtables from current order row
                    while (row.nextSibling && row.nextSibling.getAttribute('data-kt-docs-datatable-subtable') === 'subtable_template') {
                        row.nextSibling.parentNode.removeChild(row.nextSibling);
                    }
                    row.classList.remove(...rowClasses);
                    button.classList.remove('active');
                } else {
                    populateTemplate(demoData, row);
                    row.classList.add(...rowClasses);
                    button.classList.add('active');
                }
            });
        });
    }

    // Populate template with content/data -- content/data can be replaced with relevant data from database or API

    // Reset subtable
    const resetSubtable = () => {
        const subtables = document.querySelectorAll('[data-kt-docs-datatable-subtable="subtable_template"]');
        subtables.forEach(st => {
            st.parentNode.removeChild(st);
        });

        const rows = table.querySelectorAll('tbody tr');
        rows.forEach(r => {
            r.classList.remove('isOpen');
            if (r.querySelector('[data-kt-docs-datatable-subtable="expand_row"]')) {
                r.querySelector('[data-kt-docs-datatable-subtable="expand_row"]').classList.remove('active');
            }
        });
    }

    // Public methods
    return {
        init: function () {
            table = document.querySelector('#kt_docs_datatable_subtable');

            if (!table) {
                return;
            }

            initDatatable();
            handleActionButton();
        }
    }
}();

// Webpack support
if (typeof module !== 'undefined') {
    module.exports = KTDocsDatatableSubtable;
}

// On document ready
KTUtil.onDOMContentLoaded(function () {
    KTDocsDatatableSubtable.init();
});