<?php

class BDB extends SQLite3
{
	function __construct()
	{
		$this->open('/Users/blueice/git/gdoa.sqlite3');
	}
}

$db=new BDB();
$db->exec("create table gdoa(oa_id text,oa_name text,oa_com_name text,oa_dep_name text,oa_job_name text,oa_phone text,cu_mail text)");

$dom=simplexml_load_file('/Users/blueice/git/gdoa.xml');

foreach($dom->Table as $item)
{
	$sql="insert into gdoa values(";
	$sql.="'".$item->OA_ID."',";
	$sql.="'".$item->OA_NAME."',";
	$sql.="'".$item->OA_COM_NAME."',";
	$sql.="'".$item->OA_DEP_NAME."',";
	$sql.="'".$item->OA_JOB_NAME."',";
	$sql.="'".$item->OA_PHONE."',";
	$sql.="'".$item->CU_MAIL."'";
	$sql.=")";
	$db->exec($sql);
	echo $sql."\r\n";
}

?>