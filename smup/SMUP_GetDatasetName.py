

static PyObject* GetDatasetName 

(PyObject * self, PyObject * args )

[static]

得到指定数据源下指定索引位置的数据集名称 
参数:


[in]

string

strAlias 数据源别名; 



[in]

int

iIndex 指定索引位置，取值为[0, GetDatasetCount()-1]; 

返回:返回.数据源下指定位置数据集的名称. 