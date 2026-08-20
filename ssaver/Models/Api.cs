namespace ssaver.Models;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using System.Text.Encodings;
public class Api
{
    async Task<int> send(string username, string repo, string file, string token)
    {
        HttpClient client = new HttpClient();
        var data = new
        {username,repo,file,token};
        string json = JsonSerializer.Serialize(data);
        var content = new StringContent(json,Encoding.UTF8,"application/json");
        
        
        HttpResponseMessage res = await client.PostAsync(url, content);    
        
    }
}