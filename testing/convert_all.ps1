
function Convert($path)
{
    docker run -it -v ${pwd}/${path}:/data minlag/mermaid-cli -i /data/index.template.md -o /data/index.png
    py .\parse_markdown.py $path
    pandoc -s ${path}/index.md -o ${path}/index.html --metadata title="$path"
    Remove-Item ${path}/index.md
}
function GetFiles($path = './documentation')
{
    foreach ($item in Get-ChildItem $path)
    {
        #if ($exclude | Where {$item -like $_}) { continue }

        $item
        if (Test-Path $item.FullName -PathType Container)
        {
            GetFiles $item.FullName
            Convert($item.FullName)
            
        }
    }
}

GetFiles