from pathlib import Path
import zipfile,json
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'extension/manifest.json').read_text())
output=root/'dist';output.mkdir(exist_ok=True)
name=root.name+'-'+manifest['version']+'.zip'
with zipfile.ZipFile(output/name,'w',zipfile.ZIP_DEFLATED) as archive:
 for path in sorted((root/'extension').rglob('*')):
  if not path.is_file(): continue
  relative=path.relative_to(root/'extension')
  if str(relative)=='manifest.json':
   store_manifest=dict(manifest)
   store_manifest.pop('key',None)
   archive.writestr('manifest.json',json.dumps(store_manifest,ensure_ascii=False,indent=2)+'\n')
  else: archive.write(path,relative)
print(output/name)
