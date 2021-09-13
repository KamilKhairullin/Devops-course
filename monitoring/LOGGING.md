# Creating docker-compose.yml
1. Create logs network
2. Add *app with port 5000*, *loki with port 3100*, *promtail*, *grafna with port 3000*, *prometheus with port 9090* images 
3. Add *promtail.yml* config
4. Run 
```
docker-compose up
```
5. Go to 
```
localhost:3000
```
6. login to console
7. Add *Loki* data source 
8. Explore metrics

# Best practices for Loki
- Static labels are good
- Use dynamic labels sparingly
- Label values must always be bounded
- Be aware of dynamic labels applied by clients