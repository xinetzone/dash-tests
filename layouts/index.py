from dash import dcc, html

example_names = ['/examples/intro', '/examples/callback', '/examples/figure-n-slider',
                 '/examples/multiple-inputs', '/examples/multiple-outputs',
                 '/examples/chained-callback', '/examples/table-callback',
                 '/examples/state-callback', '/examples/print-graph',
                 '/examples/hover-update-graph', '/examples/cross-filter',
                 '/examples/prevent-update', '/examples/no-update',
                 '/examples/callback-context', '/examples/first-load',
                 '/examples/indirect-result', '/examples/prevent-initial-call',
                 '/examples/sync-slider-text', '/examples/convert-temperature',
                 '/examples/sync-checklists', '/examples/clientside-callbacks',
                 '/examples/clientside-callbacks-px', '/examples/all-pattern',
                 '/examples/match-pattern', '/examples/allsmaller-pattern',
                 '/examples/todo', '/examples/store-clicks', '/examples/reusable-components',
                 '/examples/external-resources', '/examples/live-update',
                 '/examples/share-data-callbacks', '/examples/simple-slider',
                 '/examples/simple-range-slider', '/examples/mark-range-slider'
                 ]

layout = html.Div([
    html.H1('Sansty Dash', className='w3-center'),
    html.Article([
        html.Header(html.H2('Dash 示例', className='w3-center')),
        *[dcc.Link(name, href=name,
                 className='w3-padding') for name in example_names],
    ], className='w3-pale-blue w3-padding')
])
