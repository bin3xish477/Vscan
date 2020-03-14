# Vscan
An antivirus project

#### Utilizing VirusTotal's v3 API to upload and analyze file
```python
resp = subp.run(f'curl --request POST \
  			--url https://www.virustotal.com/api/v3/files \
  			--header "x-apikey: {API_KEY}" \
  			--form file=@{file_path}', shell=True, stdout=subp.PIPE,
  			stderr=subp.DEVNULL)
```
----------------------------------------------------------------------------------------------------------------------------------------

#### Utilizing VirusTotal's v3 API to retrieve the uploaded file report
```python
resp = subp.run(f'curl --request GET \
	  		--url https://www.virustotal.com/api/v3/files/{sha256_hash} \
	  		--header "x-apikey: {API_KEY}"', shell=True, stdout=subp.PIPE,
	  		stderr=subp.DEVNULL)
```

# Installation
```bash
cd /opt

git clone https://github.com/binexisHATT/Vscan.git

cd /Vscan

# make sure python3-pip is installed -> sudo apt install python3-pip
pip3 install -r requirements
```
