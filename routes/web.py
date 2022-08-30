from masonite.routes import Route

ROUTES = [
    Route.get('/', "TaskController@index").name('index'),
    Route.get('/createtask', "TaskController@create").name('create'),
    Route.post('/storetask', "TaskController@store").name('store'),
    Route.get('/tasks/@id', "TaskController@show").name('show'),
    Route.get('/edit/@id', "TaskController@edit").name('edit'),
    Route.post('/update/@id', "TaskController@update").name('update'),
    Route.get('/delete/@id', "TaskController@destroy").name('destroy'),
]
