"""
获取影像文件像素格式 
参数:


[in]string strType 文件类型; ?fileTIF
 ?fileIMG
 ?fileBMP
 ?fileJPG
 ?fileGRD
 ?fileRAW
 ?fileUSGSGRID
 ?fileSIT
 ?fileArcinfoGrid
 ?fileIDR 

[in]string strFilePath 文件全路径名; 

返回:影像数据位深(字符值),与GetImagePixelFormat相对应.取值为: ?IPF_UNKNOWN
 ?IPF_MONO // 1位,单色
 ?IPF_FBIT //4位,16色
 ?IPF_BYTE //8位,256色
 ?IPF_TBYTE //16位,彩色
 ?IPF_RGB //24位,真彩色
 ?IPF_RGBA //32位,增强真彩色
 ?IPF_TRGB //48位,真彩色
 ?IPF_LONGLONG //64位,长整型
 ?IPF_LONG //32位,整型
 ?IPF_FLOAT //32位,浮点型
 ?IPF_DOUBLE //64位,双精度浮点型 

"""

